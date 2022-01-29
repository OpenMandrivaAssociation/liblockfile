%define	major	1
%define	libname	%mklibname lockfile %major
%define	devname	%mklibname lockfile -d
%define	devstatic	%mklibname lockfile -d -s

%define _disable_lto 1

Summary:	NFS-safe locking library
Name:		liblockfile
Version:	1.17
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://packages.qa.debian.org/liblockfile
Source0:	http://ftp.debian.org/debian/pool/main/libl/liblockfile/%{name}_%{version}.orig.tar.gz

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

%package -n	%{devstatic}
Summary:	NFS-safe locking development library
Group:		Development/C
Provides:	lockfile-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n	%{devstatic}
This package contains header file and development libraries.

%prep 
%autosetup -p1
# remove -g root from install
sed -i "s/-g root//" Makefile.in

%build
%configure --enable-shared --prefix=%{buildroot} --bindir=%{buildroot}%{_bindir} --mandir=%{buildroot}%{_mandir} --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir}
%make

%install
export DESTDIR=%{buildroot}
make install

%files -n dotlockfile
%{_bindir}/dotlockfile
%{_mandir}/man1/dotlockfile.1*

%files -n %{libname}
%{_libdir}/liblockfile.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/lockfile.h
%{_includedir}/maillock.h
%{_libdir}/liblockfile.so
%{_mandir}/man3/lockfile_create.3*
%{_mandir}/man3/maillock.3*

%files -n %{devstatic}
%{_libdir}/liblockfile.a
