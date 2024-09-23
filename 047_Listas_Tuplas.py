############################################################################################################

fullname = ("Grace", "M", "Hooper")

###########################################################################################################


# Funcion que convierte segundos en horas
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
type(result)
print(result)

hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
#############################################################################################################


def file_size(file_info):
    name, tipe, tam = file_info
    return "{:.2f}".format(tam / 1024)


print(file_size(("Class Assignment", "docx", 17875)))  # Should print 17.46
print(file_size(("Notes", "txt", 496)))  # Should print 0.48
print(file_size(("Program", "py", 1239)))  # Should print 1.21


#############################################################################################################
