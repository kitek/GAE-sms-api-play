GAE-sms-api-play
====================
Niniejsza aplikacja jest adaptacją skryptu do wysyłania SMS'ów [smsplay](http://code.google.com/p/smsplay/).
Do wysłania wiadomości niezbędne jest posiadanie konta (numeru) w sieci [Play](http://www.play.pl/) wraz z dostępnymi środkami (pakiet SMS, abonament).

Wysłanie wiadomości odbywa się poprzez wysłanie do serwera odpowiedniego zapytania HTTP GET zawierającego następujące parametry:

* **login** - email lub numer telefonu
* **password** - hasło do naszego konta
* **to** - numer telefonu do którego chcemy wysłać wiadomość (wraz z kierunkowym np 48)
* **body** - treść wiadomości (przygotowana przez funkcję [urlencode](http://www.opinionatedgeek.com/dotnet/tools/urlencode/Encode.aspx)), nie powinna być dłuższa niż 160 znaków

Przykłady użycia:

    https://kiteksms.appspot.com/?login=605123456&password=tajnehaslo&to=48609123456&body=Testowy+sms+do+Ciebie

Błędy i komunikaty wyjściowe:

* **OK** - SMS został wysłany
* **ERROR 1** - brak parametru login
* **ERROR 2** - brak parametru password
* **ERROR 3** - brak parametru to
* **ERROR 4** - brak parametru body
* **ERROR 5** - ogólny błąd wysłania wiadomości

Wymagane zależności (Python):

* [gaemechanize2](http://code.google.com/p/gaemechanize2/)
* re
* urllib, urllib2


Licencja:

Projekt ten rozprowadzany jest na licencji [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)