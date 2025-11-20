# 03 Active Waiting

Messung der Latenz für aktives Warten (Spinlocks) auf macOS.

## Varianten

- aw_atomic  
  Nutzt C11-Atomics (`atomic_flag`)  
- aw_unfair  
  Nutzt Apples `os_unfair_lock` (in `<os/lock.h>`)

## Kompilieren

```bash
cd "03 Active Waiting"
make all
```

## Ausführen

```bash
# atomic_flag-Variante
./aw_atomic [ITERATIONS]

# os_unfair_lock-Variante
./aw_unfair [ITERATIONS]
```

Standardmäßig wird `ITERATIONS = 10000000` genutzt, kann als Argument überschrieben werden.

## Ausgabe

- Mean, Min, Max, Stddev in Nanosekunden  
- 95 % Konfidenzintervall  

## Nächste Schritte

- CSV-Output (Option `--csv`)  
- Python-Skript zum Plotten (matplotlib)  
- Vergleich Intel vs Apple Silicon  
- Integration in den Abschlussbericht