# Created by: Sunpoet Po-Chuan Hsieh <sunpoet@FreeBSD.org>
# $FreeBSD$

PORTNAME=	public_suffix_service
PORTVERSION=	0.9.1
PORTREVISION=	19
CATEGORIES=	dns rubygems
MASTER_SITES=	RG

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Parse and decompose domain names into TLD, domain, and subdomains

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

PATCH_DEPENDS=	public_suffix_list>=0:dns/public_suffix_list

NO_ARCH=	yes
USE_RUBY=	yes
USES=		gem

post-patch:
	@${CP} ${LOCALBASE}/share/public_suffix_list/public_suffix_list.dat ${WRKSRC}/lib/public_suffix/definitions.txt

.include <bsd.port.mk>
