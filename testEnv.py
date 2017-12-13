import sys


def is_virtualenv():
    return ((hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
# The check for sys.real_prefix covers venv,
# the equality of non-empty sys.base_prefix with  sys.prefix covers virtualenv.

def is_venv():
    return hasattr(sys, 'real_prefix')
# Consider a script that uses the function like this:
print('\nIs there a real_prefix attribute? ' + str(hasattr(sys, 'real_prefix')) )




if is_venv():
	print('\ninside venv')
	print('\nThis entry should point to the original python installation directory')
	print('sys real prefix is: ' + str(sys.real_prefix) )

	print('\nThese entries should point to the virtual environment''s directory')
	print('sys prefix is: ' + sys.prefix)
	print('sys exec prefix is: ' + sys.exec_prefix)


else:
	if is_virtualenv():
		print('\ninside virtualenv')

		print('\nThe following should point to the base installation of Python')
		print('sys base prefix is: ' + sys.base_prefix)
		print('sys base exec prefix is: ' + sys.base_exec_prefix)

		print('\nThese entries should point to the virtual environment''s directory')
		print('sys prefix is: ' + sys.prefix)
		print('sys exec prefix is: ' + sys.exec_prefix)


	else:
	    print('\noutside virtualenv or venv')
