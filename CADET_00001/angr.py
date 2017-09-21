#!/usr/bin/env python
import angr

def main():
	project = angr.Project("./CADET_00001.adapted")
	explorer = project.surveyors.Explorer(find=(0x080487d8,), avoid=(0x080487ac,))
	explorer.run()
	print explorer.found[0]
	return explorer.found[0].state.posix.dumps(0).strip('\0\n')

if __name__ == '__main__':
    print main()

