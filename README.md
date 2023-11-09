# DNS-Einstellungsänderungsskript

Dieses Python-Skript ermöglicht es Ihnen, die DNS-Einstellungen Ihres Systems zu ändern. Es ist besonders nützlich, wenn Sie Ihre DNS-Server-Adressen schnell ändern müssen.

## Abhängigkeiten

Das Skript verwendet die folgenden Python-Module:

- `sys`
- `ausgabe`
- `ipv4_change`
- `einstellungen_anzeigen`

Stellen Sie sicher, dass diese Module installiert und importiert sind, bevor Sie das Skript ausführen.

## Verwendung

Das Skript führt die folgenden Schritte aus:

1. Es konfiguriert die gewünschten DNS-Server. Sie können die Variablen `primary_dns_ipv4` und `secondary_dns_ipv4` auf die gewünschten Werte setzen.
2. Es leert die Log-Einträge in der Datei `dns_settings.log`.
3. Es zeigt die aktuellen Netzwerkeinstellungen an.
4. Es zeigt die neuen DNS-Einstellungen an, die angewendet werden sollen.
5. Es fordert den Benutzer auf, die Änderungen zu bestätigen.
6. Es ändert die DNS-Einstellungen mit der Funktion `ipv4_change.change_dns_settings()`.
7. Es zeigt die Netzwerkeinstellungen nach der Änderung an.
8. Es fordert den Benutzer auf, das Skript zu beenden.

Das Skript fängt auch `KeyboardInterrupt`-Ausnahmen ab und beendet das Skript ordnungsgemäß, wenn der Benutzer es während der Ausführung abbricht.

## Hinweis

Bitte verwenden Sie dieses Skript mit Vorsicht, da eine Änderung der DNS-Einstellungen Auswirkungen auf Ihre Netzwerkverbindung haben kann. Es wird empfohlen, dass Sie wissen, was Sie tun, bevor Sie dieses Skript verwenden.
