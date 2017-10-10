from cx_Freeze import setup, Executable

setup(
	name = "SnakePY" ,
	version = "0.1" ,
	description = "Ce snake est realise sous python" ,
	executables = [Executable("snake.py")] ,
	)