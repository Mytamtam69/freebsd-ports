# $FreeBSD$

PORTNAME=	pc-networkmanager
PORTVERSION=	201710031301
CATEGORIES=	sysutils

MAINTAINER=	jt@ixsystems.com
COMMENT=	TrueOS Qt based network manager

LICENSE=	BSD2CLAUSE

ONLY_FOR_ARCHS=	amd64

LIB_DEPENDS=	libtrueos-ui.so:sysutils/trueos-libqt5

MAKE_ARGS=	PREFIX=${STAGEDIR}${PREFIX}

CONFLICTS=	pcbsd-utils*
MAKE_JOBS_UNSAFE=	yes

USES=		qmake shebangfix tar:xz
USE_LDCONFIG=	yes
USE_QT5=	core gui network svg linguist \
		buildtools x11extras widgets
USE_GL+=	gl

QMAKE_ARGS=	CONFIG+="configure"

USE_GITHUB=	yes
GH_ACCOUNT=	trueos
GH_PROJECT=	pc-networkmanager
GH_TAGNAME=	ae50abf3ba522a7685f275157455f6d424453bb2

.include <bsd.port.mk>
