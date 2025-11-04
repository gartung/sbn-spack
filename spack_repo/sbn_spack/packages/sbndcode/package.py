# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

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


class Sbndcode(CMakePackage):
    """The eponymous package of the Sbn experiment
    framework for particle physics experiments.
    """

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sbncode"
    git = "https://github.com/SBNSoftware/sbndcode"
    url = f"{git}/archive/v09_32_00.tar.gz"
    list_url = "https://github.com/SBNSoftware/sbndcode/tags"

    version("develop", branch="develop", git=f"{git}.git", get_full_repo=True)
    version("10.11.01", sha256="2bbe19cd94fafccacaef8ed819cb4cc41cd77e527a4939648eec2d8067329898")
    version("10.10.03.03", sha256="2d783202f12abd2fee6d29ef715736e60c938cffd6a8b4fe5af6825f53e4eb26")
    version("10.10.03.02", sha256="cc93880954a900e483edc2fbb4b0230da4d85e1832713e04223414c6420c1d03")
    version("10.10.03.01", sha256="67b2ed074bc79631266d7edb92088926f3f50f113e97a864cc24b32cd237a71c")
    version("10.10.03", sha256="a9a74b0bfb04569bbb1a98096c24f2fac28e72eaa1452001cad4aafac592de84")
    version("10.10.02", sha256="73e6ddbc4ca7cdc97da7ac85713b92c8fe5ea485af249a58582f60c57f9f8989")
    version("10.09.00", sha256="4a942fd7d221a653f1d4453c1cc5e09e7c2733fcd4f4feec59432b101ce9557a")
    version("10.06.03", sha256="48644beff632924698601640d17d8cbfb02c3cfbb51f242bd6ba52de1fb49b8f")
    version("10.06.00.05", sha256="87a11c57b17cfb6ed14923684e0f3b5b2282574f5a7264d86286bb696bd32977")
    version("10.06.00.04", sha256="2b6687a0da39a5eecff8be9434b9242f8e10ca1bb5122b5eb7334cb6fa3d5451")
    version("09.32.00", sha256="def738f4df92fc75d818041af15ce48fea9842dad96ea96d2285793b1f161bbf")

    patch("v09_32_00.patch", when="@9.32.00")

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
    depends_on("artdaq-core", type=("build", "run"))
    depends_on("art-root-io", type=("build", "run"))
    depends_on("art", type=("build", "run"))
    depends_on("artdaq-core", type=("build", "run"))
    depends_on("boost", type=("build", "run"))
    depends_on("canvas-root-io", type=("build", "run"))
    depends_on("canvas", type=("build", "run"))
    depends_on("cetlib-except", type=("build", "run"))
    depends_on("clhep", type=("build", "run"))
    depends_on("cppgsl", type=("build", "run"))
    depends_on("eigen", type=("build", "run"))
    depends_on("fftw", type=("build", "run"))
    depends_on("hep-concurrency", type=("build", "run"))
    depends_on("messagefacility", type=("build", "run"))
    depends_on("nlohmann-json", type=("build", "run"))
    depends_on("vdt", type=("build", "run"))
    depends_on("catch2", type=("build", "run"))
    depends_on("ifdh-art", type=("build", "run"))
    depends_on("tbb", type=("build", "run"))
    depends_on("geant4", type=("build", "run"))
    depends_on("geant4reweight", type=("build", "run"))
    depends_on("xerces-c", type=("build", "run"))
    depends_on("larana", type=("build", "run"))
    depends_on("larcoreobj", type=("build", "run"))
    depends_on("larcorealg", type=("build", "run"))
    depends_on("larcore", type=("build", "run"))
    depends_on("lardataobj", type=("build", "run"))
    depends_on("lardataalg", type=("build", "run"))
    depends_on("lardata", type=("build", "run"))
    depends_on("larevt", type=("build", "run"))
    depends_on("pandorasdk", type=("build", "run"))
    depends_on("pandoramonitoring", type=("build", "run"))
    depends_on("larpandora", type=("build", "run"))
    depends_on("larpandoracontent", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("larreco", type=("build", "run"))
    depends_on("larrecodnn", type=("build", "run"))
    depends_on("larsim", type=("build", "run"))
    depends_on("larvecutils", type=("build", "run"))
    depends_on("libwda", type=("build", "run"))
    depends_on("marley", type=("build", "run"))
    depends_on("nug4", type=("build", "run"))
    depends_on("artg4tk", type=("build", "run"))
    depends_on("nugen", type=("build", "run"))
    depends_on("nuevdb", type=("build", "run"))
    depends_on("genie", type=("build", "run"))
    depends_on("ifdhc", type=("build", "run"))
    depends_on("libxml2", type=("build", "run"))
    depends_on('nurandom', type=('build','run')) 
    depends_on('nusimdata', type=('build','run')) 
    depends_on("nutools", type=("build", "run"))
    depends_on("nufinder", type=("build", "run"))
    depends_on("postgresql", type=("build", "run"))
    depends_on("range-v3", type=("build", "run"))
    depends_on("sbndaq-artdaq-core", type=("build", "run"))
    depends_on("sqlite", type=("build", "run"))
    depends_on("trace", type=("build", "run"))
    depends_on("dk2nudata", type=("build", "run"))
    depends_on("dk2nugenie", type=("build", "run"))
    depends_on("cry", type=("build", "run"))
    depends_on("sbnanaobj", type=("build", "run"))
    depends_on("sbncode", type=("build", "run"))
    depends_on("larcv2", type=("build", "run"))
    depends_on("rstartree", type=("build", "run"))
    depends_on("protobuf", type=("build", "run"))
    depends_on("larfinder", type=("build", "run"))
    depends_on("triton", type=("build", "run"))
    depends_on("py-tensorflow", type=("build", "run"))
    depends_on("torch-scatter", type=("build", "run"))
    depends_on("hep-hpc", type=("build", "run"))

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
            "-DIGNORE_ABSOLUTE_TRANSITIVE_DEPENDENCIES=1",
            "-DTensorFlow_ROOT:FILEPATH={0}".format(tdir),
            "-DTensorFlow_cc_LIBRARY:FILEPATH={0}/libtensorflow_cc.so.2".format(tdir),
            "-DTensorFlow_framework_LIBRARY:FILEPATH={0}/libtensorflow_framework.so.2".format(tdir),
        ]
        return args

    def setup_build_environment(self, spack_env):
        # Binaries.
        spack_env.prepend_path("PATH", os.path.join(self.build_directory, "bin"))
        # Ensure we can find plugin libraries.
        spack_env.prepend_path("CET_PLUGIN_PATH", os.path.join(self.build_directory, "lib"))
        # Ensure Root can find headers for autoparsing.
        for d in self.spec.traverse(
            root=False, cover="nodes", order="post", deptype=("link"), direction="children"
        ):
            spack_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
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
