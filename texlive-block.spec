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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A style file for use with the letter class that overwrites the \opening
and \closing macros so that letters can be styled with the block letter
style instead of the default style. Thus, the return address, the
closing, and the signature appear flushed on the left margin.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/block
%dir %{_datadir}/texmf-dist/tex/latex/block
%doc %{_datadir}/texmf-dist/doc/latex/block/block.pdf
%doc %{_datadir}/texmf-dist/doc/latex/block/block.tex
%{_datadir}/texmf-dist/tex/latex/block/block.sty
