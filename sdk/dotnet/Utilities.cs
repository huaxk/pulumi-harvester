// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.IO;
using System.Reflection;
using Pulumi;

namespace Pulumi.Harvester
{
    static class Utilities
    {
        public static string? GetEnv(params string[] names)
        {
            foreach (var n in names)
            {
                var value = Environment.GetEnvironmentVariable(n);
                if (value != null)
                {
                    return value;
                }
            }
            return null;
        }

        static string[] trueValues = { "1", "t", "T", "true", "TRUE", "True" };
        static string[] falseValues = { "0", "f", "F", "false", "FALSE", "False" };
        public static bool? GetEnvBoolean(params string[] names)
        {
            var s = GetEnv(names);
            if (s != null)
            {
                if (Array.IndexOf(trueValues, s) != -1)
                {
                    return true;
                }
                if (Array.IndexOf(falseValues, s) != -1)
                {
                    return false;
                }
            }
            return null;
        }

        public static int? GetEnvInt32(params string[] names) => int.TryParse(GetEnv(names), out int v) ? (int?)v : null;

        public static double? GetEnvDouble(params string[] names) => double.TryParse(GetEnv(names), out double v) ? (double?)v : null;

        public static InvokeOptions WithVersion(this InvokeOptions? options)
        {
            if (options?.Version != null)
            {
                return options;
            }
            return new InvokeOptions
            {
                Parent = options?.Parent,
                Provider = options?.Provider,
                Version = Version,
            };
        }

        private readonly static string version;
        public static string Version => version;

        static Utilities()
        {
            var assembly = typeof(Utilities).GetTypeInfo().Assembly;
            using var stream = assembly.GetManifestResourceStream("Pulumi.Harvester.version.txt");
            using var reader = new StreamReader(stream ?? throw new NotSupportedException("Missing embedded version.txt file"));
            version = reader.ReadToEnd().Trim();
            var parts = version.Split("\n");
            if (parts.Length == 2)
            {
                // The first part is the provider name.
                version = parts[1].Trim();
            }
        }
    }

    internal sealed class HarvesterResourceTypeAttribute : Pulumi.ResourceTypeAttribute
    {
        public HarvesterResourceTypeAttribute(string type) : base(type, Utilities.Version)
        {
        }
    }
}