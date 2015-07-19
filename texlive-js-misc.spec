# revision 16211
# category Package
# catalog-ctan /macros/plain/contrib/js-misc
# catalog-date 2009-11-28 12:18:01 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-js-misc
Version:	20091128
Release:	10
Summary:	Miscellaneous macros from Joachim Schrod
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/js-misc
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/js-misc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/js-misc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A bunch of packages, including: - idverb.tex, for 'short
verbatim'; - xfig.tex, for including xfig/transfig output in a
TeX document; and - cassette.tex for setting cassette labels.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091128-2
+ Revision: 752934
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091128-1
+ Revision: 718758
- texlive-js-misc
- texlive-js-misc
- texlive-js-misc
- texlive-js-misc

