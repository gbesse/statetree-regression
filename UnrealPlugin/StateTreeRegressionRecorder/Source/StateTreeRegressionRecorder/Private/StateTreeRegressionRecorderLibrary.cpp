#include "StateTreeRegressionRecorderLibrary.h"
#include "Dom/JsonObject.h"
#include "Serialization/JsonSerializer.h"
#include "Serialization/JsonWriter.h"

void UStateTreeRegressionRecorderLibrary::RecordStateTreeMarker(const FString& Scenario, const FString& State, const FString& Event, const FString& Outcome)
{
    TSharedRef<FJsonObject> Marker = MakeShared<FJsonObject>();
    Marker->SetStringField(TEXT("scenario"), Scenario);
    Marker->SetStringField(TEXT("state"), State);
    Marker->SetStringField(TEXT("event"), Event);
    Marker->SetStringField(TEXT("outcome"), Outcome);
    FString Json;
    TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&Json);
    FJsonSerializer::Serialize(Marker, Writer);
    UE_LOG(LogTemp, Display, TEXT("STREG %s"), *Json);
}
