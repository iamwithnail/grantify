__author__ = 'chris'

import xlrd
from collections import OrderedDict
import simplejson as json


def import_workbook(filename='static/gmt.xls'):
    try:
        wb = xlrd.open_workbook(filename)
    except(IOError):
        raise
    return wb

def import_sheet(workbook, sheetname='OPEN UK GRANTS'):
    sheet = workbook.sheet_by_index(1)
    return sheet

def transform_date_from_row(row_value):
    from datetime import date
    initial = xlrd.xldate_as_tuple(row_value,0)
    output_date = date(initial[0], initial[1], initial[2])
    return output_date

def read_sheet(sheet, open=False):
    grants_list = []
    from datetime import datetime

    for rownum in range(2, sheet.nrows):
        row_values = sheet.row_values(rownum)
        try:
            grant = {
            'Funder': row_values[0],
            'Programme': row_values[1],
            'Competition': row_values[2],
            'Actions': row_values[3],
            'Overview': row_values[4],
            'Themes': row_values[5],
            'Costs': row_values[6],
            'Opens': transform_date_from_row(row_values[7]),
            'RegistrationCloses': transform_date_from_row(row_values[8]),
            'Closes': transform_date_from_row(row_values[9]),
            'MatchFund': row_values[10],
            'Partnerships': row_values[11],
            'OrgType': row_values[12],
            'OrgRestrictions': row_values[13],
            'TRL': row_values[14],
            'Location': row_values[15],
            'URL': row_values[16],
            'Contact': row_values[17]}
        except ValueError:
            grant = {
            'Funder': row_values[0],
            'Programme': row_values[1],
            'Competition': row_values[2],
            'Actions': row_values[3],
            'Overview': row_values[4],
            'Themes': row_values[5],
            'Costs': row_values[6],
            'Opens': "",
            'RegistrationCloses': "",
            'Closes': "",
            'MatchFund': row_values[10],
            'Partnerships': row_values[11],
            'OrgType': row_values[12],
            'OrgRestrictions': row_values[13],
            'TRL': row_values[14],
            'Location': row_values[15],
            'URL': row_values[16],
            'Contact': row_values[17]}
        grants_list.append(grant)
    return grants_list


def jsonify(list):
    return json.dumps(list)

def build_json():
    workbook = import_workbook()
    sheet = import_sheet(workbook)
    bare_grants_list = read_sheet(sheet)
    #grant_detail = jsonify(bare_grants_list)
    return bare_grants_list
