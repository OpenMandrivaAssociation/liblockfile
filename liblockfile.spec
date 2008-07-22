%define name	liblockfile
%define version	1.06.1
%define release	%mkrel 3

%define	major	1

%define	libname	%mklibname lockfile %major
%define	dlibname	%mklibname lockfile %major -d
%define	pdlibname	%mklibname lockfile -d

Summary:	NFS-safe locking library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		http://packages.qa.debian.org/liblockfile
BuildRoot:	%_tmppath/%{name}-%{version}-root-%(id -u -n)
Source0:	http://ftp.debian.org/debian/pool/main/libl/liblockfile/liblockfile_1.06.1.tar.bz2
Patch0:		liblockfile-1.06.1-eaccess.patch

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
%if %{_lib} != lib
Provides:	liblockfile-devel = %{version}-%{release}
%endif
Provides:	%pdlibname = %{version}-%{release}
Requires:	%libname = %{version}-%{release}

%description -n	%dlibname
Liblockfile is a library that contains NFS-safe locking functions. It also
contains an implementation of the SVR4 maillock() functions.
This package contains header file and development libraries.

%prep 
%setup -q
%patch0 -p1 -b .eaccess

%build
%configure --enable-shared
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
%doc README liblockfile.lsm debian/changelog
%{_libdir}/liblockfile.so.1
%{_libdir}/liblockfile.so.1.0

%files -n %dlibname
%defattr(-,root,root,755)
%{_includedir}/lockfile.h
%{_includedir}/maillock.h
%{_libdir}/liblockfile.a
%{_libdir}/liblockfile.so
%{_mandir}/man3/lockfile_create.3*
%{_mandir}/man3/maillock.3*



