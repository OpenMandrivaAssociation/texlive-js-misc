%global tl_name js-misc
%global tl_revision 16211

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Miscellaneous macros from Joachim Schrod
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/js-misc
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/js-misc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/js-misc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A bunch of packages, including: idverb.tex, for 'short verbatim';
xfig.tex, for including xfig/transfig output in a TeX document; and
cassette.tex for setting cassette labels.

