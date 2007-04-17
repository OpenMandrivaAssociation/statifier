%define version 1.6.10
%define release %mkrel 1

Name:		statifier
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Summary:	Convert elf dynamic linked exe to "pseudo-static"
Source:		http://prdownloads.sourceforge.net/statifier/%{name}-%{version}.tar.bz2
Url:		http://%{name}.sourceforge.net	
ExclusiveArch:	%ix86 alpha x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:  glibc-static-devel
Requires:	gdb

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
chmod -R u+w %buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README TODO
%attr(755,root,root)	%{_bindir}/statifier
%dir %{_prefix}/lib/statifier
%attr(755,root,root)	%{_prefix}/lib/statifier/*
%{_mandir}/man1/statifier.1*


