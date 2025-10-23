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


class Sbnobj(CMakePackage):
    """The eponymous package of the Sbn experiment
    framework for particle physics experiments.
    """

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sbnobj"
#    git_base = "https://cdcvs.fnal.gov/projects/sbnobj"
    git_base = "https://github.com/SBNSoftware/sbnobj"
    git = f"{git_base}.git"
    url = f"{git_base}/archive/v10_03_00.tar.gz"
    list_url = "https://github.com/SBNSoftware/sbnobj/tags"

    version(
        "develop",
        commit="821c5e24aa509b4e1ba0eda064d3ce5f3fbce1a2",
        git=git,
        get_full_repo=True,
    )
    version("10.03.00", sha256="d5b96c6d63d2deec94a3abab426925303f4bde40209b6270b1fa41a9a83f2689")
    version("10.02.02", sha256="513cc5f122bbc78ac78a36da53b8d24bd5361d68e376f009477f05e598a2dc7e")
    version("10.02.01", sha256="619910e7419f493c37121c318c9d77c00024ff87a8489e79875ebfad14dd5232")
    version("10.02.00", sha256="bc5722291985be4e2c1d25680dec0c1bf8ed357261d6c1f1724eacf401085385")
    version("10.01.02", sha256="0cd4fc9c0fec7a2e0752b4905824209d1b4bcaeb22cd9c49eafc1f358d822d9b")
    version("10.01.01.01", sha256="9a9a8a56bfac26ee2094c7c10fa47fff2f2f63027d9c0fdc47e20bbafa783454")
    version("10.01.01", sha256="5f0d85ba9598cae8ac21013cb40e5421532828b52f5c6caea7c7d45c54a43fca")
    version("10.01.00", sha256="f0df159da2b94dbd77c61f065d18b3124d44b90aee229fa4ca67c9f3aadbff53")
    version("10.00.10", sha256="9d85a03340a8cf39ad73204bb422849d49984ccc0a6b6c9c7fe01e7f17f275b3")
    version("09.19.00.02", sha256="02a785f145d4670fc943296c83e36da089f6c62c1c696dd7ba95cf025949eec6")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch("v09_12_12.patch", when="@09.12.12")
    patch("v09_12_09.patch", when="@09.12.09")
    patch("v09_12_05.patch", when="@09.12.05")
    patch("v09_12_04.patch", when="@09.12.04")
    patch("cetmodules2.patch", when="@develop")
    patch("v10_01_00.patch", when="@10.01.00")
    patch("v10_02_01.patch", when="@10.02.01")

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
    depends_on("cetlib", type=("build", "run"))
    depends_on("cetlib-except", type=("build", "run"))
    depends_on("clhep", type=("build", "run"))
    depends_on("cppgsl", type=("build", "run"))
    depends_on("eigen", type=("build", "run"))
    depends_on("fhicl-cpp", type=("build", "run"))
    depends_on("fftw", type=("build", "run"))
    depends_on("hep-concurrency", type=("build", "run"))
    depends_on("ifdh-art", type=("build", "run"))
    depends_on("tbb", type=("build", "run"))
    depends_on("geant4", type=("build", "run"))
    depends_on("larana", type=("build", "run"))
    depends_on("larcoreobj", type=("build", "run"))
    depends_on("larcorealg", type=("build", "run"))
    depends_on("larcore", type=("build", "run"))
    depends_on("lardataobj", type=("build", "run"))
    depends_on("lardataalg", type=("build", "run"))
    depends_on("lardata", type=("build", "run"))
    depends_on("larevt", type=("build", "run"))
    depends_on("larpandora", type=("build", "run"))
    depends_on("larpandoracontent", type=("build", "run"))
    depends_on("larreco", type=("build", "run"))
    depends_on("larsim", type=("build", "run"))
    depends_on("larvecutils", type=("build", "run"))
    depends_on("libwda", type=("build", "run"))
    depends_on("marley", type=("build", "run"))
    depends_on("messagefacility", type=("build", "run"))
    depends_on("nug4", type=("build", "run"))
    depends_on("nusimdata", type=("build", "run"))
    depends_on("dk2nudata", type=("build", "run"))
    depends_on("nufinder", type=("build"))
    depends_on("nutools", type=("build", "run"))
    depends_on("postgresql", type=("build", "run"))
    depends_on("root", type=("build", "run"))
    depends_on("range-v3", type=("build", "run"))
    depends_on("sbndaq-artdaq-core", type=("build", "run"))
    depends_on("sqlite", type=("build", "run"))
    depends_on("trace", type=("build", "run"))
    depends_on("py-srproxy", type=("build", "run"))
    depends_on("catch2", type=("build", "run"))
    depends_on("nlohmann-json", type=("build", "run"))
    depends_on("vdt", type=("build", "run"))

    if "SPACKDEV_GENERATOR" in os.environ:
        generator = os.environ["SPACKDEV_GENERATOR"]
        if generator.endswith("Ninja"):
            depends_on("ninja", type="build")

    def url_for_version(self, version):
        # url = 'https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2'
        url = "https://github.com/SBNSoftware/{0}/archive/v{1}.tar.gz"
        return url.format(self.name, version.underscored)

    def cmake_args(self):
        # Set CMake args.
        args = [
             "-DCMAKE_CXX_STANDARD={0}".format(self.spec.variants["cxxstd"].value),
             "-DVDT_INCLUDE_DIR={0}".format(self.spec["vdt"].prefix.include),
             "-DVDT_LIBRARY={0}".format(self.spec["vdt"].prefix.lib),
             ]
        return args

    def setup_build_environment(self, spack_env):
        spack_env.set("CETBUILDTOOLS_VERSION", self.spec["cetmodules"].version)
        spack_env.set("CETBUILDTOOLS_DIR", self.spec["cetmodules"].prefix)
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
        # Perl modules.
        spack_env.prepend_path("PERL5LIB", os.path.join(self.build_directory, "perllib"))
        # Cleaup.
        sanitize_environments(spack_env)

    def setup_run_environment(self, run_env):
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
