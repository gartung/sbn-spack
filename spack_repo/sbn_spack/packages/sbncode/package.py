# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage


def sanitize_environments(*args):
    for env in args:
        for var in (
            "PATH",
            "CET_PLUGIN_PATH",
            "LDSHARED",
            "LD_LIBRARY_PATH",
            "DYLD_LIBRARY_PATH",
            "LIBRARY_PATH",
            "CMAKE_PREFIX_PATH",
            "ROOT_INCLUDE_PATH",
        ):
            env.prune_duplicate_paths(var)
            env.deprioritize_system_paths(var)


class Sbncode(CMakePackage):
    """The eponymous package of the Sbn experiment
    framework for particle physics experiments.
    """

    url = "https://github.com/SBNSoftware/sbncode/archive/refs/tags/v09_35_01.tar.gz"
    git = "https://github.com/SBNSoftware/sbncode.git"

    version("v10_12_02",commit="813ca27339a3aac3fcf15ef78332c1e7978fa389", submodules=True)
    version("v10_11_01_01",commit="30569b2615f93ab698d68a84beb21e5bc031cd5c", submodules=True)
    version("v10_06_00_01", commit="fb929f3d9ac910bec5da48ca8adcc1bad0412eb6", submodules=True)
    version("v10_04_07", commit="412514c73b41c88fcbd9ffcf0632ed186703a2d3", submodules=True)
    version("v10_04_06_p01",commit="41ef8493069b0f07287e43ed66873484c0a203d5", submodules=True)
    version("v10_04_04",commit="d49df6743d95631d6c9edc2ae01ee3f3e3a5c01f", submodules=True)
    version("v09_93_01_p01", commit="b67723df67c57e7325c4baf3825760c6683f1c7a", submodules=True)
    version("v09_93_01_p02", commit="45baa22ccf40934ca65f5c5229df4c52ad1f7fbb", submodules=True)

    version("develop", branch="develop", submodules=True, get_full_repo=True)

    patch("artdaq-core-v4.0.patch", when="^artdaq-core@v4:")


    def patch(self):
        filter_file(
            r'find_package\( art REQUIRED \)',
            'find_package( art REQUIRED )\nfind_package(Eigen)\nfind_package(larrecodnn)',
            'CMakeLists.txt',
            )

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    # Build-only dependencies.
    depends_on("cmake@3.11:")
    depends_on("cetmodules", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Build and link dependencies.

    depends_on("genie-xsec")
    depends_on("art")
    depends_on("artdaq-core")
    depends_on("art-root-io")
    depends_on("boost")
    depends_on("canvas")
    depends_on("canvas-root-io")
    depends_on("castxml")
    depends_on("cetlib-except")
    depends_on("clhep")
    depends_on("cppgsl")
    depends_on("dk2nudata")
    depends_on("dk2nugenie")
    depends_on("eigen")
    depends_on("fftw")
    depends_on("geant4")
    depends_on("geant4reweight")
    depends_on("genie")
    depends_on("gsl")
    depends_on("hep-concurrency")
    depends_on("messagefacility")
    depends_on("ifbeam")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("larana")
    depends_on("larcore")
    depends_on("larcoreobj")
    depends_on("larcorealg")
    depends_on("lardata")
    depends_on("lardataalg")
    depends_on("lardataobj")
    depends_on("larevt")
    depends_on("larfinder")
    depends_on("larpandora")
    depends_on("larpandoracontent")
    depends_on("larreco")
    depends_on("larrecodnn +tensorflow")
    depends_on("larsim")
    depends_on("libwda")
    depends_on("libxml2")
    depends_on("log4cpp")
    depends_on("marley")
    depends_on("messagefacility")
    depends_on("nucondb")
    depends_on("nug4")
    depends_on("nugen")
    depends_on("nurandom")
    depends_on("nusystematics")
    depends_on("nusimdata")
    depends_on("nutools")
    depends_on("pandorasdk")
    depends_on("postgresql")
    depends_on("py-pygccxml")
    depends_on("py-srproxy")
    depends_on("py-torch")
    depends_on("py-tensorflow")
    depends_on("range-v3")
    depends_on("sbnanaobj")
    depends_on("sbndaq-artdaq-core")
    depends_on("sbnobj")
    depends_on("sqlite")
    depends_on("systematicstools")
    depends_on("tbb")
    depends_on("trace")
    depends_on("xerces-c")
    depends_on("zlib")
    depends_on("larcv2")
    depends_on("nusystematics")
    depends_on("geant4reweight")

    depends_on("sbndata")
    depends_on("sbnalg", when="@v10_04_07:")


    if "SPACKDEV_GENERATOR" in os.environ:
        generator = os.environ["SPACKDEV_GENERATOR"]
        if generator.endswith("Ninja"):
            depends_on("ninja", type="build")

    def url_for_version(self, version):
        # url = 'https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2'
        url = "https://github.com/SBNSoftware/{0}/archive/v{1}.tar.gz"
        return url.format(self.name, version.underscored)

    @property
    def cmake_prefix_paths(self):
        return [self.prefix,
                "{0}/lib/python{1}/site-packages/torch".format(
                self.spec["py-torch"].prefix, self.spec["python"].version.up_to(2))
                ]


    def cmake_args(self):
        # Set CMake args.
        tdir = "{0}/lib/python{1}/site-packages/tensorflow".format(
                self.spec["py-tensorflow"].prefix, self.spec["python"].version.up_to(2)
                )
        args = [
            "-DCMAKE_CXX_STANDARD={0}".format(self.spec.variants["cxxstd"].value),
            "-DZLIB_ROOT={0}".format(self.spec["zlib"].prefix),
            "-DIGNORE_ABSOLUTE_TRANSITIVE_DEPENDENCIES=1",
            "-DTensorFlow_ROOT:FILEPATH={0}".format(tdir),
            "-DTensorFlow_cc_LIBRARY:FILEPATH={0}/libtensorflow_cc.so.2".format(tdir),
            "-DTensorFlow_framework_LIBRARY:FILEPATH={0}/libtensorflow_framework.so.2".format(tdir),
        ]
        return args

    def setup_build_environment(self, spack_env):
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec["root"].prefix.lib)
        # Binaries.
        spack_env.prepend_path("PATH", os.path.join(self.build_directory, "bin"))
        # Ensure we can find plugin libraries.
        spack_env.prepend_path("CET_PLUGIN_PATH", os.path.join(self.build_directory, "lib"))
        # Ensure Root can find headers for autoparsing.
        for d in self.spec.traverse(
            root=False, cover="nodes", order="post", deptype=("link"), direction="children"
        ):
            spack_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
        spack_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        # Perl modules.
        spack_env.prepend_path("PERL5LIB", os.path.join(self.build_directory, "perllib"))
        # Cleaup.
        sanitize_environments(spack_env)

    def setup_run_environment(self, run_env):
        # Binaries.
        run_env.prepend_path("PATH", os.path.join(self.prefix, "bin"))
        # Ensure we can find plugin libraries.
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        # Ensure Root can find headers for autoparsing.
        for d in self.spec.traverse(
            root=False, cover="nodes", order="post", deptype=("link"), direction="children"
        ):
            run_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        # Perl modules.
        run_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        # Cleaup.
        sanitize_environments(run_env)

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        # Binaries.
        spack_env.prepend_path("PATH", self.prefix.bin)
        # Ensure we can find plugin libraries.
        spack_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        # Ensure Root can find headers for autoparsing.
        spack_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        # Perl modules.
        spack_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        # Cleanup.
        sanitize_environments(spack_env)

    def setup_dependent_run_environment(self, run_env, dependent_spec):
        # Binaries.
        run_env.prepend_path("PATH", self.prefix.bin)
        # Ensure we can find plugin libraries.
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        # Ensure Root can find headers for autoparsing.
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        # Perl modules.
        run_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        # Cleanup.
        sanitize_environments(run_env)
