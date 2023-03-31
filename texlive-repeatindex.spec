Name:		texlive-repeatindex
Version:	24305
Release:	2
Summary:	Repeat items in an index after a page or column break
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/repeatindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}
