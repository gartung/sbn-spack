# Copyright2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

class Dummy(CMakePackage):
    """The eponymous package of the Sbn experiment
    framework for particle physics experiments.
    """

    git_base = "https://github.com/SBNSoftware/sbndcode.git"

    version("10.12.02_dev", sha256="9360544a3b9ad2dd7500d1479b1a76b52a2153169a9222eccc17153477894c9a")
    version("10.12.02", sha256="9360544a3b9ad2dd7500d1479b1a76b52a2153169a9222eccc17153477894c9a")
    version("10.06.00.01", sha256="5ad9dfb9e96adf82a9f0a6fcbcb8042664b1349fe4f44374462f17fce2d95b51")
    version("10.04.07", tag="v10_04_07", git=git_base, get_full_repo=True)
    version("10.04.06.01",tag="v10_04_06_01", git=git_base, get_full_repo=True)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("cetbuildtools", type="build")
    depends_on("cmake@3.11:")

    #depends_on("nuevdb", type=("build", "run"))
    depends_on("sbncode")
    depends_on("sbnd-data")

    def url_for_version(self, version):
        url = "https://github.com/SBNSoftware/{0}/archive/v{1}.tar.gz"
        return url.format(self.name, version.underscored)

    def cmake_args(self):
        args = [
            "--debug-find"
            ]
        return args
