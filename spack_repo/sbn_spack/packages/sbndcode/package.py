# Copyright2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

class Sbndcode(CMakePackage):
    """The eponymous package of the Sbn experiment
    framework for particle physics experiments.
    """

    git_base = "https://github.com/SBNSoftware/sbndcode.git"

    version("10.11.01.01", sha256="dae33d76ae429e1ad5f4775c0e6a0059fb44d7190471db378d7748285f4533d5")
    version("10.12.02", sha256="9360544a3b9ad2dd7500d1479b1a76b52a2153169a9222eccc17153477894c9a")
    version("10.06.00.01", sha256="5ad9dfb9e96adf82a9f0a6fcbcb8042664b1349fe4f44374462f17fce2d95b51")
    version("10.04.07", tag="v10_04_07", git=git_base, get_full_repo=True)
    version("10.04.06.01",tag="v10_04_06_01", git=git_base, get_full_repo=True)

    patch("spack.patch")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.11:")
    depends_on("cetmodules", type="build")
    depends_on("cetbuildtools", type="build")

    depends_on("libjpeg")
    depends_on("libpng")
    depends_on("giflib")
    depends_on("eigen")
    depends_on("libwda")
    depends_on("postgresql")
    depends_on("rstartree")
    depends_on("vdt")
    depends_on("fftw")
    depends_on("hep-hpc")

    depends_on("dk2nudata")
    depends_on("marley")
    depends_on("cry")
    depends_on("dk2nugenie")

    depends_on("nuevdb")
    depends_on("sbncode")
    depends_on("sbnd-data")

    if "SPACKDEV_GENERATOR" in os.environ:
        generator = os.environ["SPACKDEV_GENERATOR"]
        if generator.endswith("Ninja"):
            depends_on("ninja", type="build")

    def patch(self):
        cetmodules_version = self.spec['cetmodules'].version.string
        sbndcode_version = self.version.string.split('_')[0]
        filter_file('cetmodules REQUIRED', 'cetmodules '+cetmodules_version+' REQUIRED','CMakeLists.txt')
        filter_file('sbndcode LANGUAGES', 'sbndcode VERSION '+sbndcode_version+' LANGUAGES','CMakeLists.txt')

    def url_for_version(self, version):
        url = "https://github.com/SBNSoftware/{0}/archive/v{1}.tar.gz"
        return url.format(self.name, version.underscored)

    def cmake_args(self):
        # Set CMake args.
        args = [
            "-DIGNORE_ABSOLUTE_TRANSITIVE_DEPENDENCIES=True",
            "-DCMAKE_CXX_STANDARD={0}".format(self.spec.variants["cxxstd"].value),
            "-Dsbndcode_FW_DIR=fw",
            "-Dsbndcode_WP_DIR={0}".format(self.spec["wire-cell-toolkit"].prefix),
            "--debug-find"
            ]
        return args

    def setup_build_environment(self, spack_env):
        spack_env.prepend_path("HEP_HPC_INC", self.spec['hep-hpc'].prefix.include)
        spack_env.prepend_path("PATH", os.path.join(self.build_directory, "bin"))
        spack_env.set("SBNDCODE_DIR", str(self.build_directory))
        spack_env.prepend_path("CET_PLUGIN_PATH", os.path.join(self.build_directory, "lib"))
        for d in self.spec.traverse(
            root=False, cover="nodes", order="post", deptype=("link"), direction="children"
        ):
            spack_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
        spack_env.prepend_path("PERL5LIB", os.path.join(self.build_directory, "perllib"))
        spack_env.prepend_path("GENIE_INC", str(self.spec["genie"].prefix.include))
        spack_env.prepend_path("LD_LIBRARY_PATH", "{0}/lib/python{1}/site-packages/tensorflow".format(self.spec["py-tensorflow"].prefix, "3.10"))

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", os.path.join(self.prefix, "bin"))
        run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        run_env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix.gdml))
        run_env.prepend_path("FW_SEARCH_PATH", os.path.join(self.spec['sbnd-data'].prefix))
        run_env.prepend_path("FHICL_FILE_PATH", self.prefix.fcl)
        run_env.prepend_path("FHICL_INCLUDE_PATH", self.prefix.fcl)
        run_env.prepend_path("WIRECELL_PATH", os.path.join(self.spec['wire-cell-toolkit'].prefix))

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.prepend_path("PATH", self.prefix.bin)
        spack_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        spack_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        spack_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
