%define name	liblockfile
%define version	1.08
%define release	%mkrel 6

%define	major	1

%define	libname	%mklibname lockfile %major
%define	dlibname	%mklibname lockfile -d

Summary:	NFS-safe locking library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		http://packages.qa.debian.org/liblockfile
BuildRoot:	%_tmppath/%{name}-%{version}-root-%(id -u -n)
Source0:	http://ftp.debian.org/debian/pool/main/libl/liblockfile/%{name}_%{version}.orig.tar.gz
Patch1:		liblockfile-1.08-fix-install-perms.patch

%description
Liblockfile is a shared library with NFS-safe locking functions.
It includes the command-line utility ``dotlockfile''.

%package -n	dotlockfile
Summary:	Mailbox locking tool
Group:		Networking/Mail

%description -n dotlockfile
Dotlockfile is a command line utility to safely create, test and
remove lockfiles. Lockfiles are created in an NFS-safe way. Dotlockfile
can can also be used to lock and unlock mailboxes even if the mailspool
directory is only writable by group mail.

%package -n	%libname
Summary:	NFS-safe locking library
Group:		System/Libraries

%description -n %libname
Liblockfile is a library that contains NFS-safe locking functions. It also
contains an implementation of the SVR4 maillock() functions.
The functions in liblockfile can lock and unlock mailboxes even if special
priviliges are needed by calling an external setgid-mail utility called
`dotlockfile'.

%package -n	%dlibname
Summary:	NFS-safe locking development library
Group:		Development/C
Provides:	lockfile-devel = %{version}-%{release}
Provides:	liblockfile-devel = %{version}-%{release}
Obsoletes:	%{_lib}lockfile1-devel < %{version}-%{release}
Requires:	%libname = %{version}-%{release}

%description -n	%dlibname
Liblockfile is a library that contains NFS-safe locking functions. It also
contains an implementation of the SVR4 maillock() functions.
This package contains header file and development libraries.

%prep 
%setup -q
%patch1 -p0 -b .perm

%build
%configure2_5x --enable-shared
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_includedir} \
	$RPM_BUILD_ROOT/%{_bindir} \
	$RPM_BUILD_ROOT/%{_libdir} \
	$RPM_BUILD_ROOT/%{_mandir}/man{1,3}
make install ROOT=$RPM_BUILD_ROOT
make install_static ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n dotlockfile
%defattr(-,root,root,755)
%{_bindir}/dotlockfile
%{_mandir}/man1/dotlockfile.1*

%files -n %libname
%defattr(-,root,root,755)
%doc README liblockfile.lsm
%{_libdir}/liblockfile.so.%{major}
%{_libdir}/liblockfile.so.%{major}.*

%files -n %dlibname
%defattr(-,root,root,755)
%{_includedir}/lockfile.h
%{_includedir}/maillock.h
%{_libdir}/liblockfile.a
%{_libdir}/liblockfile.so
%{_mandir}/man3/lockfile_create.3*
%{_mandir}/man3/maillock.3*





%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.08-5mdv2011.0
+ Revision: 661485
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.08-4mdv2011.0
+ Revision: 602569
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.08-3mdv2010.1
+ Revision: 520879
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.08-2mdv2010.0
+ Revision: 425592
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 1.08-1mdv2009.1
+ Revision: 365735
- drop patch0 ,fixed upstream
- New version 1.08

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - do not use %%mkrel twice
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Aug 09 2006 Luca Berra <bluca@comedia.it>
+ 2006-08-09 14:13:44 (54694)
- add %%defattr to all %%files sections

* Wed Aug 09 2006 Luca Berra <bluca@comedia.it>
+ 2006-08-09 13:17:16 (54677)
- fix provides

* Wed Aug 09 2006 Luca Berra <bluca@comedia.it>
+ 2006-08-09 13:04:23 (54672)
- import liblockfile-1.06.1-1mdv2007.0

* Wed Aug 09 2006 Luca Berra <bluca@mandriva.org> 1.06.1-1mdv2007.0
- Initial mandriva package

