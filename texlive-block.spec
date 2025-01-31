Name:		texlive-block
Version:	17209
Release:	2
Summary:	A block letter style for the letter class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/block
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/block.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/block.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A style file for use with the letter class that overwrites the
\opening and \closing macros so that letters can be styled with
the block letter style instead of the default style. Thus, the
return address, the closing, and the signature appear flushed
on the left margin.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/block/block.sty
%doc %{_texmfdistdir}/doc/latex/block/block.pdf
%doc %{_texmfdistdir}/doc/latex/block/block.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
