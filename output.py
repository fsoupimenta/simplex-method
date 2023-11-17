import os
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill, Border, Side


def export_to_sheet(columns_header, rows_header, matrix, last_row_filled, columns_to_color=None, row_to_color=None):
    file_name = "simplex.xlsx"
    if os.path.exists(file_name):
        workbook = load_workbook(file_name)
        worksheet = workbook.active
    else:
        workbook = Workbook()
        worksheet = workbook.active

    color_fill = PatternFill(start_color='5F9F9F', end_color='5F9F9F', fill_type='solid')
    border_style = Border(left=Side(border_style='thin'), right=Side(border_style='thin'),
                          top=Side(border_style='thin'), bottom=Side(border_style='thin'))

    for i, column in enumerate(columns_header):
        worksheet.cell(row=last_row_filled, column=i + 2, value=column)

    for j, row in enumerate(rows_header):
        worksheet.cell(row=last_row_filled + j + 1, column=1, value=row)

    for a, row in enumerate(matrix):
        for b, column in enumerate(row):
            worksheet.cell(row=last_row_filled + a + 1, column=b + 2, value=column)

    if columns_to_color is not None:
        for col in range(1, len(columns_header) + 2):
            worksheet.cell(row=last_row_filled + row_to_color + 1, column=col).fill = color_fill

        for row in range(last_row_filled, last_row_filled + len(rows_header) + 1):
            worksheet.cell(row=row, column=columns_to_color + 2).fill = color_fill

    for row in worksheet.iter_rows(min_row=last_row_filled, max_row=last_row_filled + len(rows_header), min_col=1,
                                   max_col=len(columns_header) + 1):
        for cell in row:
            cell.border = border_style

    workbook.save(file_name)
