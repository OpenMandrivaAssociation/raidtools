%define name	raidtools
%define version	0.90
%define release	%mkrel 14

Summary:	Tools for creating and maintaining software RAID devices.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/raid/alpha/raidtools-19990824-0.90.tar.bz2
Patch0:		raidtools-0.90-64bit-lseek.patch.bz2
Patch1:		raidtools-0.90-variable-pagesize.patch.bz2
Patch2:		raidtools-0.90-warnings.patch.bz2
Obsoletes:	md, md-tools
Provides:	md md-tools
Conflicts:	kernel < 2.2
Requires:	dev >= 3.0.2-4mdk, common-licenses

%description
This package includes the tools you need to set up and maintain a software RAID
device under Linux. It only works with Linux 2.2 kernels and later, or 2.0
kernel specifically patched with newer raid support.

%prep
%setup -q
%patch0 -p1 -b .64bit-lseek
%patch1 -p1 -b .variable-pagesize
%patch2 -p1 -b .warnings

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./autogen.sh
%make

%install
%make ROOTDIR=$RPM_BUILD_ROOT MAN=%{_mandir} install_bin install_doc

# (fg) 20000828 These devices are now in dev
#
#for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
#  mknod -m 0600 $RPM_BUILD_ROOT/dev/md$i b 9 $i
#done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/*
%{_mandir}/*/*
%doc README *.sample
%doc Software-RAID.HOWTO/Software-RAID.HOWTO.txt

