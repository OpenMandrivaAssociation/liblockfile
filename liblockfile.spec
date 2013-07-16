%define	major	1
%define	libname	%mklibname lockfile %major
%define	devname	%mklibname lockfile -d

Summary:	NFS-safe locking library
Name:		liblockfile
Version:	1.09
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://packages.qa.debian.org/liblockfile
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

%package -n	%{libname}
Summary:	NFS-safe locking library
Group:		System/Libraries

%description -n %{libname}
Liblockfile is a library that contains NFS-safe locking functions. It also
contains an implementation of the SVR4 maillock() functions.
The functions in liblockfile can lock and unlock mailboxes even if special
priviliges are needed by calling an external setgid-mail utility called
`dotlockfile'.

%package -n	%{devname}
Summary:	NFS-safe locking development library
Group:		Development/C
Provides:	lockfile-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains header file and development libraries.

%prep 
%setup -q
%patch1 -p0 -b .perm

%build
%configure2_5x --enable-shared
%make

%install
mkdir -p %{buildroot}/%{_includedir} \
	%{buildroot}/%{_bindir} \
	%{buildroot}/%{_libdir} \
	%{buildroot}/%{_mandir}/man{1,3}
make install ROOT=%{buildroot}

%files -n dotlockfile
%{_bindir}/dotlockfile
%{_mandir}/man1/dotlockfile.1*

%files -n %{libname}
%doc README liblockfile.lsm
%{_libdir}/liblockfile.so.%{major}*

%files -n %{devname}
%{_includedir}/lockfile.h
%{_includedir}/maillock.h
%{_libdir}/liblockfile.so
%{_mandir}/man3/lockfile_create.3*
%{_mandir}/man3/maillock.3*

