%define version 1.7.2
%define release 2

Name:		statifier
Version:	%{version}
Release:	1
License:	GPLv2
Group:		Development/Other
Summary:	Convert elf dynamic linked exe to "pseudo-static"
Source:		http://prdownloads.sourceforge.net/statifier/%{name}-%{version}.tar.gz
Url:		https://%{name}.sourceforge.net	
ExclusiveArch:	%ix86 alpha x86_64
BuildRequires:  glibc-static-devel
Requires:      coreutils
Requires:      gawk
Requires:      gdb

%description
Statifier create from dynamically linked ELF executable
and all it's libraries (and all LD_PRELOAD libraries if any)
one file. This file can be copied and run on another machine
without need to drag all it's libraries.

%prep
%setup -q

%build
make all

%install

%makeinstall_std
chmod -R u+w %buildroot


%files
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README TODO
%attr(755,root,root)	%{_bindir}/statifier
%dir %{_prefix}/lib/statifier
%attr(755,root,root)	%{_prefix}/lib/statifier/*
%{_mandir}/man1/statifier.1*


