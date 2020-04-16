# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'es'
dateSep = ['/']
usesMeridian = False
uses24 = True
decimal_mark = ','

Weekdays = [
    'lunes', 'martes', 'miércoles|miercoles',
    'jueves', 'viernes', 'sábado|sabado', 'domingo',
]
shortWeekdays = [
    'lun', 'mar', 'mié|mie',
    'jue', 'vie', 'sáb|sab', 'dom',
]
Months = [
    'enero', 'febrero', 'marzo',
    'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre',
    'octubre', 'noviembre', 'diciembre',
]
shortMonths = [
    'ene', 'feb', 'mar',
    'abr', 'may', 'jun',
    'jul', 'ago', 'sep',
    'oct', 'nov', 'dic',
]
dateFormats = {
    'full': "EEEE d' de 'MMMM' de 'yyyy",
    'long': "d' de 'MMMM' de 'yyyy",
    'medium': "dd-MMM-yy",
    'short': "d/MM/yy",
}

timeFormats = {
    'full': "HH'H'mm' 'ss z",
    'long': "HH:mm:ss z",
    'medium': "HH:mm:ss",
    'short': "HH:mm",
}

dp_order = ['d', 'm', 'y']


dayOffsets = {
    'mañana': 1,
    'hoy': 0,
    'ayer': -1,
}


numbers = {
    'cero': 0,
    'uno': 1,
    'un': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5,
    'seis': 6,
    'siete': 7,
    'ocho': 8,
    'nueve': 9,
    'diez': 10,
    'once': 11,
    'doce': 12,
    'trece': 13,
    'catorce': 14,
    'quince': 15,
    'dieciseis': 16,
    'diecisiete': 17,
    'dieciocho': 18,
    'diecinueve': 19,
    'veinte': 20
}


units = {
    'seconds': ['segundo', 'segundos', 'seg', 'segs', 'sec', 'secs', 's'],
    'minutes': ['minuto', 'minutos', 'min', 'mins', 'm'],
    'hours': ['hora', 'horas', 'hr', 'h'],
    'days': ['dia', 'dias', 'd'],
    'weeks': ['semana', 'semanas', 'sem'],
    'months': ['mes', 'meses'],
    'years': ['año', 'años'],
}

# TODO: Understand and Translate Modifiers, re_values, ignore
# TODO: Translate re_sources, small, magnitude
# TODO: Understand and Fix dateFormats
# TODO: Unit tests for Spanish Locale
