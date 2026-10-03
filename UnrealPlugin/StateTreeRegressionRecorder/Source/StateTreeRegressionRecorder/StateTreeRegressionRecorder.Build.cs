using UnrealBuildTool;

public class StateTreeRegressionRecorder : ModuleRules
{
    public StateTreeRegressionRecorder(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine" });
        PrivateDependencyModuleNames.AddRange(new string[] { "Json" });
    }
}
