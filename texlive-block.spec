# revision 17209
# category Package
# catalog-ctan /macros/latex/contrib/block
# catalog-date 2010-02-26 11:17:49 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-block
Version:	20100226
Release:	1
Summary:	A block letter style for the letter class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/block
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/block.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/block.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A style file for use with the letter class that overwrites the
\opening and \closing macros so that letters can be styled with
the block letter style instead of the default style. Thus, the
return address, the closing, and the signature appear flushed
on the left margin.

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
%{_texmfdistdir}/tex/latex/block/block.sty
%doc %{_texmfdistdir}/doc/latex/block/block.pdf
%doc %{_texmfdistdir}/doc/latex/block/block.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
