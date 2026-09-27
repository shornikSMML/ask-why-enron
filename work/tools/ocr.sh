#!/bin/bash
# OCR an image-only library PDF into work/text/<id>.txt, one "=== PAGE n ===" marker per page.
# Usage: ocr.sh <manifest-id> <pdf path>. The original PDF is never changed.
export OMP_THREAD_LIMIT=1
id=$1; pdf=$2; tmp=work/ocr-tmp/$id; mkdir -p $tmp
n=$(pdfinfo "$pdf" | awk '/^Pages:/{print $2}')
seq 1 $n | xargs -P 4 -I{} sh -c "[ -s $tmp/{}.txt ] || { pdftoppm -r 200 -gray -f {} -l {} -png '$pdf' $tmp/p{}; tesseract $tmp/p{}*.png $tmp/{} >/dev/null 2>&1; rm -f $tmp/p{}*.png; }"
: > work/text/$id.txt
for i in $(seq 1 $n); do printf '\n=== PAGE %s ===\n' $i >> work/text/$id.txt; cat $tmp/$i.txt >> work/text/$id.txt 2>/dev/null; done
echo "$id done ($n pages)"
