%global tl_name phfnote
%global tl_revision 60733

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0
Release:	%{tl_revision}.1
Summary:	Basic formatting for short documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phfnote
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfnote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfnote.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfnote.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides basic formatting for short documents such as notes
on a specific topic, short documentation, or quick memos. It aims to
cover all basic needs for such purposes: include a standard set of
relevant packages, a nice title which doesn't take up too much space,
better page margin sizes, and some basic styling to make the note look
nicer. At the same time, it is highly flexible and customizable.

