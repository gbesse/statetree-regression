# StateTree Regression

Compare ordered StateTree scenario markers across Unreal game builds. The optional Blueprint function `Record State Tree Marker` writes a compact `STREG` JSON line to the Unreal log. Call it from the states or tasks you want to assert, then compare two run logs:

```sh
python3 statetree_regression.py examples/baseline.log examples/current.log
python3 -m unittest discover -s tests
```

The comparison checks `scenario`, `state`, `event` and `outcome` in order, ignoring timestamps and unrelated log lines. Exit code 1 means a scenario differs. To use the recorder, copy `UnrealPlugin/StateTreeRegressionRecorder` into your project's `Plugins` directory, enable it, and call the Blueprint function at relevant state entries and exits. `event` can be `Enter`, `Exit` or a project-defined marker. This does **not** parse `.utrace` files or replace Epic's [StateTree Debugger](https://dev.epicgames.com/documentation/unreal-engine/statetree-debugger-quick-start-guide). The Python comparator is tested; the Unreal plugin still needs an Unreal Editor build to confirm engine compatibility.

## Français

Comparez les marqueurs émis par vos scénarios StateTree entre deux versions d’un jeu. Le module Blueprint écrit des lignes `STREG` dans le journal Unreal ; l’outil Python compare leur ordre et leurs résultats. Un écart fait échouer la commande. Le module Unreal doit encore être compilé dans l’éditeur.

## Español

Compare los marcadores emitidos por escenarios StateTree entre dos versiones de un juego. El módulo Blueprint escribe líneas `STREG` en el registro de Unreal; la herramienta Python compara su orden y sus resultados. Una diferencia hace fallar el comando. El módulo Unreal aún debe compilarse en el editor.

MIT licensed.
