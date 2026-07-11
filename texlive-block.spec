%global tl_name block
%global tl_revision 17209

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A block letter style for the letter class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/block
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/block.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/block.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A style file for use with the letter class that overwrites the \opening
and \closing macros so that letters can be styled with the block letter
style instead of the default style. Thus, the return address, the
closing, and the signature appear flushed on the left margin.

