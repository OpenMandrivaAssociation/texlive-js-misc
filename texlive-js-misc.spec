Name:		texlive-js-misc
Version:	20091128
Release:	1
Summary:	Miscellaneous macros from Joachim Schrod
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/js-misc
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/js-misc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/js-misc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A bunch of packages, including: - idverb.tex, for 'short
verbatim'; - xfig.tex, for including xfig/transfig output in a
TeX document; and - cassette.tex for setting cassette labels.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/js-misc/cassette.tex
%{_texmfdistdir}/tex/plain/js-misc/idverb.tex
%{_texmfdistdir}/tex/plain/js-misc/js-misc.tex
%{_texmfdistdir}/tex/plain/js-misc/schild.tex
%{_texmfdistdir}/tex/plain/js-misc/sperr.tex
%{_texmfdistdir}/tex/plain/js-misc/xfig.tex
%doc %{_texmfdistdir}/doc/plain/js-misc/History
%doc %{_texmfdistdir}/doc/plain/js-misc/INSTALL
%doc %{_texmfdistdir}/doc/plain/js-misc/Imakefile
%doc %{_texmfdistdir}/doc/plain/js-misc/License
%doc %{_texmfdistdir}/doc/plain/js-misc/Makefile
%doc %{_texmfdistdir}/doc/plain/js-misc/README
%doc %{_texmfdistdir}/doc/plain/js-misc/TODO
%doc %{_texmfdistdir}/doc/plain/js-misc/deutsch.doc
%doc %{_texmfdistdir}/doc/plain/js-misc/deutsch.tex
%doc %{_texmfdistdir}/doc/plain/js-misc/idverb.doc
%doc %{_texmfdistdir}/doc/plain/js-misc/names.sty
%doc %{_texmfdistdir}/doc/plain/js-misc/xfig/text-2.1-doc.tex
%doc %{_texmfdistdir}/doc/plain/js-misc/xfig/text-2.1.fig
%doc %{_texmfdistdir}/doc/plain/js-misc/xfig/text-2.1.latex
%doc %{_texmfdistdir}/doc/plain/js-misc/xfig/text-3.1-doc.tex
%doc %{_texmfdistdir}/doc/plain/js-misc/xfig/text-3.1.latex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
