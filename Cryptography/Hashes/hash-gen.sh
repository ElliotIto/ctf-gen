#/bin/bash
hash="$1sum"
file="$2"
output="$3"
hashsum="$(echo $hash | tr '[:upper:]' '[:lower:]')"
echo "Outputting $hashsum of lines in $file to $output" 
while read line; do
	echo -n "$line" | $hashsum | awk '{print $1}' >> "$output"
done <$file
