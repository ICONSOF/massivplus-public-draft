---
layout: default_banner
title: "Förslag"
nav_order: 4
has_children: true
has_toc: false
permalink: /forslag/
---

# Förslag

Förslag till ändringar i standarden. Ett förslag ingår inte i standarden förrän ett releasemöte har antagit det. Hur ett förslag går från idé till beslut beskrivs i [Så utvecklas standarden](../sa-utvecklas-standarden.md), och [mallen](mall.md) visar vad ett förslag innehåller.

{%- assign alla = site.pages | where: "parent", "Förslag" | where_exp: "p", "p.forslag_id" | sort: "forslag_id" -%}
{%- assign beredda = alla | where: "forslag_status", "Beredd" -%}
{%- assign diskussion = alla | where: "forslag_status", "Under diskussion" -%}
{%- assign utkast = alla | where: "forslag_status", "Utkast" -%}
{%- assign avgjorda = alla | where_exp: "p", "p.forslag_status == 'Antagen' or p.forslag_status == 'Avvisad' or p.forslag_status == 'Parkerad'" %}

## Inför releasemötet {{ site.massiv.nasta_releasemote }} (version {{ site.massiv.nasta_version }})

{% include forslagstabell.html lista=beredda tom="Inga förslag är beredda inför mötet ännu." %}

## Under diskussion

{% include forslagstabell.html lista=diskussion tom="Inga förslag är under diskussion just nu." %}

## Utkast

{% include forslagstabell.html lista=utkast tom="Inga utkast just nu." %}

## Avgjorda

{% include forslagstabell.html lista=avgjorda tom="Inga förslag har avgjorts ännu." beslut=true %}
