
cd  /media/tw/SSD
cd  3_CodeEditor/Geany/ConfigurationFilesBackup

cp -vu   ~/.config/geany/*.conf                       .
cp -vu   ~/.config/geany/ui_toolbar.xml               .
cp -vu   ~/.config/geany/Save_to_SSD.sh               .

mkdir -v   filedefs
cp -vu   ~/.config/geany/filedefs/filetypes*          filedefs

mkdir -v   templates/files
cp -vu   ~/.config/geany/templates/files/*            templates/files

mkdir -v   colorschemes
cp -vu   ~/.config/geany/colorschemes/*               colorschemes

