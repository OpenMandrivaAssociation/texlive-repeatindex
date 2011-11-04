# revision 24305
# category Package
# catalog-ctan /macros/latex/contrib/repeatindex
# catalog-date 2011-06-16 21:20:53 +0200
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-repeatindex
Version:	0.01
Release:	1
Summary:	Repeat items in an index after a page or column break
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/repeatindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This Package repeats item of an index if a page or column break
occurs within a list of subitems. This helps to find out to
which main item a subitem belongs.

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
%{_texmfdistdir}/makeindex/repeatindex/repeatindex.ist
%{_texmfdistdir}/tex/latex/repeatindex/repeatindex.sty
%doc %{_texmfdistdir}/doc/latex/repeatindex/README
%doc %{_texmfdistdir}/doc/latex/repeatindex/testrepeatindex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
