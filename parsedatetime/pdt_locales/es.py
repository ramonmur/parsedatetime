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

re_sources = {
    'mediodia': {'hr': 12, 'mn': 0, 'sec': 0},
    'mediodía': {'hr': 12, 'mn': 0, 'sec': 0},
    'media_mañana': {'hr': 11, 'mn': 0, 'sec': 0},
    'media_tarde': {'hr': 17, 'mn': 0, 'sec': 0},
    'comida': {'hr': 14, 'mn': 0, 'sec': 0},
    'desayuno': {'hr': 8, 'mn': 0, 'sec': 0},
    'cena': {'hr': 21, 'mn': 0, 'sec': 0},
    'medianoche': {'hr': 0, 'mn': 0, 'sec': 0},
    'alba': {'hr': 6, 'mn': 0, 'sec': 0},
    'amanecer': {'hr': 6, 'mn': 0, 'sec': 0},
    'atardecer': {'hr': 19, 'mn': 0, 'sec': 0},
}


small = {
    'cero': 0,
    'uno': 1,
    'un': 1,
    'una': 1,
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
    'veinte': 20,
    'veintiuno': 21,
    'veintidós': 22,
    'veintidos': 22,
    'veintitrés': 23,
    'veintitres': 23,
    'veinticuatro': 24,
    'veinticinco': 25,
    'veintiséis': 26,
    'veintiseis': 26,
    'veintisiete': 27,
    'veintiocho': 28,
    'veintinueve': 29,
    'treinta': 30,
    'cuarenta': 40,
    'cincuenta': 50,
    'sesenta': 60,
    'setenta': 70,
    'ochenta': 80,
    'noventa': 90,
    'cien': 100,
    'doscientos': 200,
    'trescientos': 300,
    'cuatrocientos': 400,
    'quinientos': 500,
    'seiscientos': 600,
    'setecientos': 700,
    'ochocientos': 800,
    'novecientos': 900,

}

magnitude = {
    'mil': 10**3,
    'millon': 10**6,
    'millón': 10**6,
    'millones': 10**6,
    'billon': 10**12,
    'billón': 10**12,
    'billones': 10**12,
    'trillón': 10**18,
    'trillon': 10**18,
    'trillones': 10**18,
    'cuatrillón': 10**24,
    'cuatrillon': 10**24,
    'cuatrillones': 10**24,
    'quintillón': 10**30,
    'quintillon': 10**30,
    'quintillones': 10**30,
    'sextillón': 10**36,
    'sextillon': 10**36,
    'sextillones': 10**36,
    'septillón': 10**42,
    'septillon': 10**42,
    'septillones': 10**42,
    'octillón': 10**48,
    'octillon': 10**48,
    'octillones': 10**48,
    'nonallón': 10**54,
    'nonallon': 10**54,
    'nonallones': 10**54,
    'decillón': 10**60,
    'decillon': 10**60,
    'decillones': 10**60,
}

# TODO: Understand and Translate Modifiers, re_values, ignore
# TODO: Understand and Fix dateFormats
# TODO: Unit tests for Spanish Locale
