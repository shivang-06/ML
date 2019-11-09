
import cgi
import predict

form=cgi.FieldStorage()

review=form.getvalue('review')

pred=predict.test(review)


if pred==0:
    msg="Negative"
else:
    msg="Positive"

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sentiment Analysis</title>
</head>
<body>

<h5>Sentiment predicted is : {}</h5>
</body>
</html>
""".format(msg))
