Name:		texlive-phfnote
Version:	60733
Release:	1
Summary:	Basic formatting for short documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfnote
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfnote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfnote.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfnote.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides basic formatting for short documents such
as notes on a specific topic, short documentation, or quick
memos. It aims to cover all basic needs for such purposes:
include a standard set of relevant packages, a nice title which
doesn't take up too much space, better page margin sizes, and
some basic styling to make the note look nicer. At the same
time, it is highly flexible and customizable.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfnote
%{_texmfdistdir}/tex/latex/phfnote
%{_texmfdistdir}/bibtex/bst/phfnote
%doc %{_texmfdistdir}/doc/latex/phfnote

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
