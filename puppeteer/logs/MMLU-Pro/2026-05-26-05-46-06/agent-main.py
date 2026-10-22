def check_cell_division_control():
    # Define the options related to cell division control
    control_options = ['Microtubules', 'Checkpoints', 'DNA polymerase', 'Centrosomes', 'Cyclins', 'Protein kinases', 'Fibroblast cells']
    print("Control Options:", control_options)

    # Define the options not related to cell division control
    non_control_options = ['Mitochondria', 'DNA polymerase', 'Fibroblast cells']
    print("Non-Control Options:", non_control_options)

    # Find the option that is not known to be involved in the control of cell division
    not_controlled = [option for option in non_control_options if option in control_options]
    print("Options not involved in cell division control:", not_controlled)

    # Return the result
    return not_controlled

print(check_cell_division_control())