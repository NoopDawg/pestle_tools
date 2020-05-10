import os

def write_args(args, out_path, to_file=True, filename='config.txt'):
    options = vars(args)
    if to_file:
         with open(os.path.join(out_path, filename), 'w+') as f:
             for option in options:
                 f.write("{}: {}\n".format(option, options[option]))
                 print("{}: {}".format(option, options[option]))
    else:
        for option in options:
            print("{}: {}".format(option, options[option]))

