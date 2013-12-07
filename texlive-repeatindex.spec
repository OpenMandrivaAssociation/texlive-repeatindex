# revision 24305
# category Package
# catalog-ctan /macros/latex/contrib/repeatindex
# catalog-date 2011-06-16 21:20:53 +0200
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-repeatindex
Version:	0.01
Release:	3
Summary:	Repeat items in an index after a page or column break
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/repeatindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This Package repeats item of an index if a page or column break
occurs within a list of subitems. This helps to find out to
which main item a subitem belongs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/repeatindex/repeatindex.ist
%{_texmfdistdir}/tex/latex/repeatindex/repeatindex.sty
%doc %{_texmfdistdir}/doc/latex/repeatindex/README
%doc %{_texmfdistdir}/doc/latex/repeatindex/testrepeatindex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.01-2
+ Revision: 755660
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.01-1
+ Revision: 719450
- texlive-repeatindex
- texlive-repeatindex
- texlive-repeatindex
- texlive-repeatindex

