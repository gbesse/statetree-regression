#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "StateTreeRegressionRecorderLibrary.generated.h"

UCLASS()
class STATETREEREGRESSIONRECORDER_API UStateTreeRegressionRecorderLibrary : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "Testing|StateTree Regression")
    static void RecordStateTreeMarker(const FString& Scenario, const FString& State, const FString& Event, const FString& Outcome);
};
