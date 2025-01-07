# Some unseful BASH coomns

Extract chars

```
echo "database" | cut -c1-4
echo "database" | cut -c1,5
```

Extract columns

```
cut -d":" -f1 /etc/passwd
cut -d":" -f1,3,6 /etc/passwd
cut -d":" -f3-6 /etc/passwd
```

Translate

```
echo "Shell Scripting" | tr "[a-z]" "[A-Z]"
echo "Shell Scripting" | tr "[:lower:]" "[:upper:]"
``` 

Translate multiple
```
ps | tr -s " "
ps | tr -s "[:space:]"
```

Delete chars

```
echo "My login pin is 5634" | tr -d "[:digit:]"
```

