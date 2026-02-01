# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

#libdir = "%s/var/spack/repos/fnal_art/lib" % os.environ["SPACK_ROOT"]
#if libdir not in sys.path:
#    sys.path.append(libdir)
#
#
#def patcher(x):
#    cetmodules_20_migrator(".", "artg4tk", "9.07.01")


#def sanitize_environments(*args):
#    for env in args:
#        for var in (
#            "PATH",
#            "CET_PLUGIN_PATH",
#            "LDSHARED",
#            "LD_LIBRARY_PATH",
#            "DYLD_LIBRARY_PATH",
#            "LIBRARY_PATH",
#            "CMAKE_PREFIX_PATH",
#            "ROOT_INCLUDE_PATH",
#        ):
#            env.prune_duplicate_paths(var)
#            env.deprioritize_system_paths(var)


class Sbnobj(CMakePackage):
    """The eponymous package of the Sbn experiment
    framework for particle physics experiments.
    """

    git_base = "https://github.com/SBNSoftware/sbnobj.git"

    version("10.03.01", sha256="2c4e1c79a3b823d507ee9708aeec66951fb1539e31dc911fb02567acc809d24c")
    version("10.01.00", sha256="f0df159da2b94dbd77c61f065d18b3124d44b90aee229fa4ca67c9f3aadbff53")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch("spack.patch")
    patch("cetmodules2.patch", when="@develop")

    depends_on("c", type="build")
    depends_on("cxx", type="build")


    # Build-only dependencies.
    depends_on("cmake@3.11:")
    depends_on("cetmodules", type="build")

    # Build and link dependencies.
    #depends_on("artdaq-core", type=("build", "run"))
    #depends_on("art-root-io", type=("build", "run"))
    depends_on("art", type=("build", "run"))
    #depends_on("artdaq-core", type=("build", "run"))
    depends_on("boost", type=("build", "run"))
    #depends_on("canvas-root-io", type=("build", "run"))
    depends_on("canvas", type=("build", "run"))
    #depends_on("cetlib", type=("build", "run"))
    #depends_on("cetlib-except", type=("build", "run"))
    depends_on("clhep", type=("build", "run"))
    #depends_on("cppgsl", type=("build", "run"))
    #depends_on("eigen", type=("build", "run"))
    #depends_on("fhicl-cpp", type=("build", "run"))
    depends_on("fftw", type=("build", "run"))
    #depends_on("hep-concurrency", type=("build", "run"))
    #depends_on("ifdh-art", type=("build", "run"))
    #depends_on("tbb", type=("build", "run"))
    #depends_on("larana", type=("build", "run"))
    depends_on("larcoreobj", type=("build", "run"))
    depends_on("larcorealg", type=("build", "run"))
    depends_on("larcore", type=("build", "run"))
    depends_on("lardataobj", type=("build", "run"))
    depends_on("lardataalg", type=("build", "run"))
    depends_on("lardata", type=("build", "run"))
    #depends_on("larevt", type=("build", "run"))
    #depends_on("larpandora", type=("build", "run"))
    #depends_on("larpandoracontent", type=("build", "run"))
    #depends_on("larreco", type=("build", "run"))
    #depends_on("larsim", type=("build", "run"))
    #depends_on("libwda", type=("build", "run"))
    #depends_on("marley", type=("build", "run"))
    depends_on("messagefacility", type=("build", "run"))
    #depends_on("nug4", type=("build", "run"))
    depends_on("nusimdata", type=("build", "run"))
    depends_on("dk2nudata", type=("build", "run"))
    #depends_on("nutools", type=("build", "run"))
    #depends_on("postgresql", type=("build", "run"))
    depends_on("root", type=("build", "run"))
    #depends_on("vdt", type=("build", "run"))
    #depends_on("sbndaq-artdaq-core", type=("build", "run"))
    #depends_on("sqlite", type=("build", "run"))
    #depends_on("trace", type=("build", "run"))
    #depends_on("py-srproxy", type=("build", "run"))

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
        args = ["-DCMAKE_CXX_STANDARD={0}".format(self.spec.variants["cxxstd"].value),
                "-DFFTW3_PREFIX={0}".format(self.spec['fftw'].prefix),
                "-DSQLite3_INCLUDE_DIR={0}".format(self.spec['sqlite'].prefix.include),
                "-DSQLite3_LIBRARY={0}".format(self.spec['sqlite'].prefix.lib),
                "-DPostgreSQL_INCLUDE_DIR={0}".format(self.spec['postgresql'].prefix.include),
                "-DPostgreSQL_LIBRARY={0}".format(self.spec['postgresql'].prefix.lib),
                "-DFFTW3_INCLUDE_DIR={0}".format(self.spec['fftw'].prefix.include),
                "-DFFTW3_LIBRARY={0}".format(self.spec['fftw'].prefix.lib),
                "-DVDT_INCLUDE_DIR={0}".format(self.spec['vdt'].prefix.include),
                "-DVDT_LIBRARY={0}".format(self.spec['vdt'].prefix.lib)]
        return args

    def setup_build_environment(self, spack_env):
    #    spack_env.set("CETBUILDTOOLS_VERSION", self.spec["cetmodules"].version)
    #    spack_env.set("CETBUILDTOOLS_DIR", self.spec["cetmodules"].prefix)
    #    spack_env.prepend_path("LD_LIBRARY_PATH", self.spec["root"].prefix.lib)

    #    # Binaries.
    #    spack_env.prepend_path("PATH", os.path.join(self.build_directory, "bin"))
    #    # Ensure we can find plugin libraries.
    #    spack_env.prepend_path("CET_PLUGIN_PATH", os.path.join(self.build_directory, "lib"))
    #    # Ensure Root can find headers for autoparsing.
    #    for d in self.spec.traverse(
    #        root=False, cover="nodes", order="post", deptype=("link"), direction="children"
    #    ):
    #        spack_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
    #    # Perl modules.
    #    spack_env.prepend_path("PERL5LIB", os.path.join(self.build_directory, "perllib"))

        #spack_env.prepend_path("CMAKE_MODULE_PATH", self.spec['fftw'].prefix.lib.cmake.fftw3)
        #spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['fftw'].prefix.lib.cmake.fftw3)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['intel-tbb'].prefix.lib64.cmake.TBB)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['catch2'].prefix.lib64.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['larvecutils'].prefix.lib.larvecutils.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['nlohmann-json'].prefix.share.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['nufinder'].prefix.lib.nufinder.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['range-v3'].prefix.lib64.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['cetlib'].prefix.lib.cetlib.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['cetlib-except'].prefix.lib.cetlib_except.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['fhicl-cpp'].prefix.lib.fhiclcpp.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['hep-concurrency'].prefix.lib.hep_concurrency.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['canvas-root-io'].prefix.lib.canvas_root_io.cmake)
        spack_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['art-root-io'].prefix.lib.art_root_io.cmake)
        # Cleaup.
        #sanitize_environments(spack_env)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", os.path.join(self.prefix, "bin"))
        # Ensure we can find plugin libraries.
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        run_env.prepend_path("CMAKE_PREFIX_PATH", self.spec['catch2'].prefix.lib64.cmake)
        # Ensure Root can find headers for autoparsing.
        #for d in self.spec.traverse(
        #    root=False,
        #    cover="nodes",
        #    order="post",
        #    deptype=("link"),
        #    direction="children",
        #):
        #    run_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
        #run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        # Perl modules.
        run_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        # Cleaup.
        #sanitize_environments(run_env)

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
        #sanitize_environments(spack_env)
