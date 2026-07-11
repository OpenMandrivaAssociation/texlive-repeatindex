%global tl_name repeatindex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Repeat items in an index after a page or column break
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/repeatindex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/repeatindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This Package repeats item of an index if a page or column break occurs
within a list of subitems. This helps to find out to which main item a
subitem belongs.

