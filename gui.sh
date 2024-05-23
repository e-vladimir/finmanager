#/bin/sh

export PYTHONPATH=$PYTHONPATH:./G0
export PYTHONPATH=$PYTHONPATH:./G1
export PYTHONPATH=$PYTHONPATH:./G2
export PYTHONPATH=$PYTHONPATH:./G3

export PYTHONPATH=$PYTHONPATH:./L0
export PYTHONPATH=$PYTHONPATH:./L1
export PYTHONPATH=$PYTHONPATH:./L2
export PYTHONPATH=$PYTHONPATH:./L3
export PYTHONPATH=$PYTHONPATH:./L4
export PYTHONPATH=$PYTHONPATH:./L5
export PYTHONPATH=$PYTHONPATH:./L6
export PYTHONPATH=$PYTHONPATH:./L7
export PYTHONPATH=$PYTHONPATH:./L8
export PYTHONPATH=$PYTHONPATH:./L9

export PYTHONPATH=$PYTHONPATH:./ui/form_export
export PYTHONPATH=$PYTHONPATH:./ui/form_finactions
export PYTHONPATH=$PYTHONPATH:./ui/form_finanalytics
export PYTHONPATH=$PYTHONPATH:./ui/form_findata
export PYTHONPATH=$PYTHONPATH:./ui/form_findescription
export PYTHONPATH=$PYTHONPATH:./ui/form_finstatistic
export PYTHONPATH=$PYTHONPATH:./ui/form_finstuct
export PYTHONPATH=$PYTHONPATH:./ui/form_import
export PYTHONPATH=$PYTHONPATH:./ui/form_main
export PYTHONPATH=$PYTHONPATH:./ui/form_record_finaction
export PYTHONPATH=$PYTHONPATH:./ui/form_record_findata
export PYTHONPATH=$PYTHONPATH:./ui/form_record_rules
export PYTHONPATH=$PYTHONPATH:./ui/form_reset
export PYTHONPATH=$PYTHONPATH:./ui/form_rules
export PYTHONPATH=$PYTHONPATH:./ui/form_backups

python3 -u gui_finmanager.py
