# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage


class Sbnanaobj(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/SBNSoftware/sbnanaobj/archive/refs/tags/v09_17_04.tar.gz"
    git_base="https://github.com/SBNSoftware/sbnanaobj.git"
    git = git_base
    list_url = "https://github.com/SBNSoftware/sbnanaobj/tags"

    version("10.00.11", sha256="0206e96d17d0049b0f8bd779f3ad71b6a0f64d7b4febe6944952143117b0f0f4")
    version("10.00.10", sha256="1d37747e5efeff0405dfd139a43c63f88327f5c23d0373dcb7eca8475bc33c6f")
    version("10.00.09", sha256="80a15de21fbebcb3beca7131c5f6cc89ab8b8d1ca661439e8b5d943b93f4a2a8")
    version("10.00.08", sha256="8c2451d63f79663ffd5ea1ed5567bf40a92cb86dfe18f73d8423fe57f11a0d4b")
    version("10.00.07", sha256="8e2f8ebef55f19cd92e0c6e637c7ce932fa3d79c930fcdea9c711c7085427b36")
    version("10.00.06", sha256="0f98c5f0678e099a9b691327ceea8d5c749def5dc1e61342fcb82b12c20a16f6")
    version("10.00.05.02", sha256="b176d69b39d99264ccf73ec1e08224d60941406acf8c7972c77ef8fa8851e78b")
    version("10.00.05.01", sha256="1c4863afbc735d96fbb46142a7f0eea0f52a0760b77d130dbdba78c2058094a7")
    version("10.00.05", sha256="b8eced3cda133e497f3c1694f7cb742fe123cbeaee6393dfe2c24ba5679e6de5")
    version("09.23.00.03", sha256="488d2879f85532e0224fde57ede9c6b81177a489fb2b656ca32f97361a7d1a49")
    version(
        "09.17.06.06", sha256="e943ca9411282fdd1d3d8b635b706d777722857426488188b39d2bb6c9cd3947"
    )
    version("09.17.06.02", sha256="8e014ac6fe6d3472645ef444b4fb9e470a411c38c0098fd8a7df41813732f8c7")
    version(
        "09.17.06.01", sha256="4b74e17e5051af8f9c3f324199e69fbe1872a50a6f188bee205f334cac646ced"
    )
    version("09.17.04", sha256="06f4534f5b5022162fae07581a53d16ca3a7b3bd27e42738c8ce33558ca0b348")
    version("09.17.02", sha256="985796b3b49a2d3fc93984b65169593c1483e29df78c98ac6c215eae88b59b7e")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch("v09_17_06_06.patch", when="@09.17.06.06")
    patch("v09_17_06_02.patch", when="@09.17.06.02")
    patch("v09_17_06_01.patch", when="@09.17.06.01")
    patch("v09_17_04.patch", when="@09.17.04")
    patch("v09_17_02.patch", when="@09.17.02")

    depends_on("root")
    depends_on("py-srproxy")
    depends_on("castxml")
    depends_on("py-pygccxml")
    depends_on("cetmodules", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def url_for_version(self, version):
        # url = 'https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2'
        url = "https://github.com/SBNSoftware/{0}/archive/v{1}.tar.gz"
        return url.format(self.name, version.underscored)

    def cmake_args(self):
        args = ["-DCMAKE_CXX_STANDARD={0}".format(self.spec.variants["cxxstd"].value)]
        return args

    def setup_build_environment(self, spack_env):
        spack_env.set("SBNANAOBJ_DIR", "%s" % os.path.realpath(self.stage.source_path))
        spack_env.set("ROOT_INC", "%s" % self.spec["root"].prefix.include)
