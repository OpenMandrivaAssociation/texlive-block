# revision 17209
# category Package
# catalog-ctan /macros/latex/contrib/block
# catalog-date 2010-02-26 11:17:49 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-block
Version:	20100226
Release:	2
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100226-2
+ Revision: 749785
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100226-1
+ Revision: 717954
- texlive-block
- texlive-block
- texlive-block
- texlive-block
- texlive-block

